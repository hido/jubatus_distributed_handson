sudo rabbitmqctl add_user jubatus jubatus
sudo rabbitmqctl add_user jubatus_normal jubatus_normal
sudo rabbitmqctl add_user jubatus_anomaly jubatus_anomaly
sudo rabbitmqctl set_permissions -p / jubatus ".*" ".*" ".*"
sudo rabbitmqctl set_permissions -p / jubatus_analyze ".*" ".*" ".*"
sudo rabbitmqctl set_permissions -p / jubatus_anomaly ".*" ".*" ".*"
