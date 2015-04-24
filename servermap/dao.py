#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import json

class Dao(object):
    def __init__(self):
        with open("config.json") as f:
            self.config = json.loads(f.read())
        super(Dao, self).__init__()
        self.connection = sqlite3.connect(self.config["db"]["path"])
        self.cursor = self.connection.cursor()

        self.run_pragma()
        self.create_servers_table()
        self.create_dimensions_table()
        self.create_metrics_table()
        self.create_datapoints_table()

    def run_pragma(self):
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.connection.commit()

    def create_servers_table(self):
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
        self.cursor.execute(query)
        self.connection.commit()

    def create_dimensions_table(self):
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
        self.cursor.execute(query)
        self.connection.commit()

    def create_metrics_table(self):
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
        self.cursor.execute(query)
        self.connection.commit()

    def create_datapoints_table(self):
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
        self.cursor.execute(query)
        self.connection.commit()

    def save_server_data(self, server_name=None, host=None,
                         user=None, port=None,
                         key=None, password=None):
        query = u"""
            INSERT OR REPLACE INTO servers VALUES(
                ?, ?, ?, ?, ?, ?
            );
        """
        t = (server_name, host, user, port, key, password)
        self.cursor.execute(query, t)
        self.connection.commit()

    def save_dimension_data(self, dimension_name=None,
                             description=None, version=None,
                             url=None, author=None, license=None):
        query = u"""
            INSERT OR REPLACE INTO dimensions VALUES(
                ?, ?, ?, ?, ?, ?
            );
        """
        t = (dimension_name, description, version, url, author, license)
        self.cursor.execute(query, t)
        self.connection.commit()

    def save_metric_data(self, metric_name=None, dimension_name=None,
                         unit=None, value_type=None):
        query = """
            INSERT OR REPLACE INTO metrics VALUES(
                ?, ?, ?, ?
            );
        """
        t = (metric_name, dimension_name, unit, value_type)
        self.cursor.execute(query, t)
        self.connection.commit()

    def save_datapoint_data(self, dimension_name=None, metric_name=None,
                            host=None, value=None, timestamp=None):
        query = """
            INSERT INTO datapoints VALUES(
                ?, ?, ?, ?, ?
            );
        """
        t = (dimension_name, metric_name, host, value, timestamp)
        self.cursor.execute(query, t)
        self.connection.commit()

    def get_metrics_data(self, host, dim_name, met_name,
                         from_ts, to_ts):
        query = """
            SELECT *
            FROM (
                SELECT *
                FROM datapoints
                WHERE
                    datapoints.dimension_name = ? AND
                    datapoints.metric_name    = ? AND
                    datapoints.host           = ? AND
                    datapoints.timestamp BETWEEN ? AND ?
            ) dp
            LEFT JOIN metrics m ON dp.metric_name = m.metric_name
            LEFT JOIN dimensions d ON dp.dimension_name = d.dimension_name
            ORDER BY dp.timestamp ASC;
        """
        t = (host, dim_name, met_name, from_ts, to_ts)
        self.cursor.execute(query, t)
        for row in self.connection:
            print row
