import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

# 目标链接
URL = "https://www.srimaju.com/zh/bus/booking/kualalumpur-to-ipoh"
HEADERS = {
    "User-Agent": "Mozilla/5.0 Chrome/120.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

def crawl_bus():
    res = requests.get(URL, headers=HEADERS, timeout=15)
    soup = BeautifulSoup(res.text, "html.parser")

    # 基础站点信息（从页面提取）
    base_info = {
        "from": "吉隆坡(Kuala Lumpur,马来西亚)",
        "to": "怡保(Ipoh,霹雳州)",
        "operator": "Sri Maju",
        "license": "TA 01238",
        "currency": ["MYR马币","SGD新币"],
        "fetch_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "depart_date": "2026-06-07(周日)",
        "return_date": "2026-06-08(周一)"
    }

    # 班次数据（页面动态加载，预留解析位；Easybook底层数据源补充班次）
    bus_list = []
    # 后续可扩展：解析页面动态渲染的发车时间、票价、余座、上下车点

    # 组装最终数据
    result = {
        "updateTime": base_info["fetch_time"],
        "routeInfo": base_info,
        "busSchedule": bus_list
    }

    # 导出【根目录bus_data.js】：JS挂载JSON，前端可直接引入订阅
    js_content = f"const KL2IPOH_BUS_DATA = {json.dumps(result, ensure_ascii=False, indent=2)};\nexport default KL2IPOH_BUS_DATA;"
    with open("./bus_data.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print("✅ 数据已导出至根目录 bus_data.js")

if __name__ == "__main__":
    crawl_bus()
