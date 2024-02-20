# linux_exporter
基于Python Flask的Linux采集器，整合主机性能监控，进程监控，数据库监控和其他自定指标监控
增加了url地址认证，默认admin/admin
# Linux 性能指标
指标地址：http://localhost:9088/node
指标名称以node开头,支持自定义脚本指标
# Process 指标
指标地址：http://localhost:9088/process
指标名以process开头，采集config/process.yaml中的指定进程状态
# Db 指标
指标地址：http://localhost:9088/db
指标以db开头
# Other 指标
指标地址：http://localhost:9088/other
指标以custom开头，自定义指标，读取config/custom.yaml中的指标
