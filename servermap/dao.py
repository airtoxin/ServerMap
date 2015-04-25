#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import json

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class Dao(object):
    def __init__(self):
        with open("config.json") as f:
            self.config = json.loads(f.read())
        super(Dao, self).__init__()

        self.create_servers_table()
        self.create_dimensions_table()
        self.create_metrics_table()
        self.create_datapoints_table()

    def get_connection(self):
        connection = sqlite3.connect(self.config["db"]["path"])
        connection.row_factory = dict_factory
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        return (connection, cursor)

    def create_servers_table(self):
        connection, cursor = self.get_connection()
        query = u"""
            CREATE TABLE IF NOT EXISTS servers (
                server_name TEXT NOT NULL,       -- ダッシュボード等に表示するサーバー名
                host        TEXT NOT NULL,       -- hoge.example.com
                user        TEXT DEFAULT 'root', --
                port        INTEGER,             --
                key         TEXT,                -- SSH鍵ファイルへのパス
                password    TEXT,            -- SSH接続のパスワード
                PRIMARY KEY(host)
            );
        """
        cursor.execute(query)
        connection.commit()
        cursor.close()

    def create_dimensions_table(self):
        connection, cursor = self.get_connection()
        query = u"""
            CREATE TABLE IF NOT EXISTS dimensions (
                dimension_name TEXT NOT NULL, -- ダッシュボード等に表示するディメンション名
                description    TEXT,          -- 説明文
                version        TEXT,          --
                url            TEXT,          -- github等
                author         TEXT,          --
                license        TEXT,          --
                PRIMARY KEY(dimension_name)
            );
        """
        cursor.execute(query)
        connection.commit()
        cursor.close()

    def create_metrics_table(self):
        connection, cursor = self.get_connection()
        query = u"""
            CREATE TABLE IF NOT EXISTS metrics (
                metric_name    TEXT NOT NULL, -- ダッシュボード等に表示するメトリック名
                dimension_name TEXT NOT NULL, --
                unit           TEXT NOT NULL, -- データ点の単位
                value_type     TEXT NOT NULL, -- データ点の型
                PRIMARY KEY(metric_name, dimension_name),
                FOREIGN KEY(dimension_name)
                    REFERENCES dimensions(dimension_name)
            );
        """
        cursor.execute(query)
        connection.commit()
        cursor.close()

    def create_datapoints_table(self):
        connection, cursor = self.get_connection()
        query = u"""
            CREATE TABLE IF NOT EXISTS datapoints (
                dimension_name TEXT    NOT NULL, --
                metric_name    TEXT    NOT NULL, --
                host           TEXT    NOT NULL, --
                value          TEXT    NOT NULL, -- アプリケーション側で必要に応じてmetrics.value_typeを見てキャストする。
                timestamp      INTEGER NOT NULL, --
                PRIMARY KEY(dimension_name, metric_name, host, timestamp),
                FOREIGN KEY(metric_name, dimension_name)
                    REFERENCES metrics(metric_name, dimension_name),
                FOREIGN KEY(host)
                    REFERENCES servers(host)
            );
        """
        cursor.execute(query)
        connection.commit()
        cursor.close()

    def save_server_data(self, server_name=None, host=None,
                         user=None, port=None,
                         key=None, password=None):
        connection, cursor = self.get_connection()
        query = u"""
            INSERT OR REPLACE INTO servers VALUES(
                ?, ?, ?, ?, ?, ?
            );
        """
        t = (server_name, host, user, port, key, password)
        cursor.execute(query, t)
        connection.commit()
        cursor.close()

    def save_dimension_data(self, dimension_name=None,
                             description=None, version=None,
                             url=None, author=None, license=None):
        connection, cursor = self.get_connection()
        query = u"""
            INSERT OR REPLACE INTO dimensions VALUES(
                ?, ?, ?, ?, ?, ?
            );
        """
        t = (dimension_name, description, version, url, author, license)
        cursor.execute(query, t)
        connection.commit()
        cursor.close()

    def save_metric_data(self, metric_name=None, dimension_name=None,
                         unit=None, value_type=None):
        connection, cursor = self.get_connection()
        query = """
            INSERT OR REPLACE INTO metrics VALUES(
                ?, ?, ?, ?
            );
        """
        t = (metric_name, dimension_name, unit, value_type)
        cursor.execute(query, t)
        connection.commit()
        cursor.close()

    def save_datapoint_data(self, dimension_name=None, metric_name=None,
                            host=None, value=None, timestamp=None):
        connection, cursor = self.get_connection()
        query = """
            INSERT INTO datapoints VALUES(
                ?, ?, ?, ?, ?
            );
        """
        t = (dimension_name, metric_name, host, value, timestamp)
        cursor.execute(query, t)
        connection.commit()
        cursor.close()

    def get_servers(self):
        connection, cursor = self.get_connection()
        query = """
            SELECT *
            FROM servers
        """
        result = tuple(cursor.execute(query))
        cursor.close()
        return result

    def get_server_name_by_host(self, host):
        connection, cursor = self.get_connection()
        query = """
            SELECT server_name
            FROM servers
            WHERE host = ?
        """
        t = (host,)
        result = tuple(cursor.execute(query, t))[0]["server_name"]
        cursor.close()
        return result

    def get_metrics_data(self, host, from_ts, to_ts):
        connection, cursor = self.get_connection()
        query = """
            SELECT
                dp.dimension_name AS dimension_name,
                dp.metric_name AS metric_name,
                dp.timestamp AS timestamp,
                dp.value AS value,
                m.unit AS unit,
                m.value_type AS value_type
            FROM (
                SELECT *
                FROM datapoints
                WHERE
                    datapoints.host = ? AND
                    datapoints.timestamp BETWEEN ? AND ?
            ) dp
            LEFT JOIN metrics m ON dp.metric_name = m.metric_name
            ORDER BY
                dp.dimension_name ASC,
                dp.metric_name ASC,
                dp.timestamp ASC
            ;
        """
        t = (host, from_ts, to_ts)
        result = tuple(cursor.execute(query, t))
        cursor.close()
        return result

    def get_all_metrics_data(self, from_ts, to_ts):
        connection, cursor = self.get_connection()
        query = """
            SELECT
                dp.host AS host,
                s.server_name AS server_name,
                dp.dimension_name AS dimension_name,
                dp.metric_name AS metric_name,
                dp.timestamp AS timestamp,
                dp.value AS value,
                m.unit AS unit,
                m.value_type AS value_type
            FROM (
                SELECT *
                FROM datapoints
                WHERE datapoints.timestamp BETWEEN ? AND ?
            ) dp
            LEFT JOIN metrics m ON dp.metric_name = m.metric_name
            LEFT JOIN servers s ON dp.host = s.host
            ORDER BY
                dp.dimension_name ASC,
                dp.metric_name ASC,
                dp.timestamp ASC
            ;
        """
        t = (from_ts, to_ts)
        result = tuple(cursor.execute(query, t))
        cursor.close()
        return result
