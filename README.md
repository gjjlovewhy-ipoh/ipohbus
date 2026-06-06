# ipohbus
# 吉隆坡→怡保 Sri Maju大巴实时班次数据源
## 数据地址
JS订阅地址：`https://raw.githubusercontent.com/你的Github用户名/kl2ipoh-bus-spider/main/bus_data.js`
## 更新规则
- 云端GitHub Actions **每2小时自动抓取官网数据**，自动更新bus_data.js
- 前端/项目直接import引入JS即可实时获取最新大巴时刻表、票价、运营方信息
## 本地运行
1. pip install -r requirements.txt
2. python spider.py → 根目录生成bus_data.js
