#!/bin/bash
service mysql start
exec tail -f /var/log/mysql/error.log
