#!/bin/bash
service rabbitmq-server start
exec tail -f /var/log/rabbitmq/rabbit\@localhost.log
