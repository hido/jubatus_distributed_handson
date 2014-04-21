sudo rabbitmqctl add_user jubatus jubatus
sudo rabbitmqctl set_permissions -p / jubatus  ".*" ".*" ".*"
