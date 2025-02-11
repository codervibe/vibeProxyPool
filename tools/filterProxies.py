# -*- coding: utf-8 -*-
# @Time    : 24 1月 2025 6:59 下午
# @Author  : codervibe
# @File    : filterProxies.py
# @Project : vibeProxyPool
# 读取 当前目录上一层目录下的  output 目录下的 proxies.json 文件，并过滤出可用的代理 并将可用的代理输出到文件中

import os
import json
import requests


def is_proxy_available(proxy, proxy_type):
    """
    检查代理是否可用。
    :param proxy: 代理字符串，例如 "http://127.0.0.1:8080"
    :param proxy_type: 代理类型，例如 "HTTP" 或 "HTTPS"
    :return: 如果代理可用，返回 True；否则返回 False
    """
    # 根据代理类型选择合适的URL
    url = 'https://www.baidu.com/' if proxy_type.upper() == 'HTTPS' else 'http://www.baidu.com/'
    url2 = 'https://www.hao123.com/' if proxy_type.upper() == 'HTTPS' else 'http://www.hao123.com/'
    url3 = 'https://www.2345.com/' if proxy_type.upper() == 'HTTPS' else 'http://www.2345.com/'

    try:
        # 使用requests库通过代理发送GET请求
        response = requests.get(url, proxies={proxy_type.lower(): proxy}, timeout=5)
        response2 = requests.get(url2, proxies={proxy_type.lower(): proxy}, timeout=5)
        response3 = requests.get(url3, proxies={proxy_type.lower(): proxy}, timeout=5)

        # 检查响应状态码和响应内容中的origin字段是否与代理地址一致
        if (response.status_code == 200 and response.json().get('origin') == proxy.split('//')[1]
                and response2.status_code == 200 and response.json().get('origin') == proxy.split('//')[1]
                and response3.status_code == 200 and response.json().get('origin') == proxy.split('//')[1]):
            # 如果检查通过，打印代理地址并返回True
            print(f"proxy: {proxy}")
            return True
    except requests.RequestException:
        # 如果发生请求异常，不做任何处理
        pass

    # 如果检查失败或发生异常，返回False
    return False


def filter_proxies():
    # 获取当前目录的上一层目录
    parent_dir = os.getcwd()
    # print(f"{parent_dir}")
    # 构建 proxies_filter.json 文件的完整路径
    input_file_path = os.path.join(parent_dir, 'output', 'proxies.json')
    # print(f"{input_file_path}")
    # 构建输出文件的完整路径
    output_file_path = os.path.join(parent_dir, 'output', 'proxies_filter.json')

    # 读取 JSON 文件内容
    with open(input_file_path, 'r', encoding='utf-8') as file:
        proxies = json.load(file)

    # 过滤出可用的代理
    # 初始化可用代理列表
    available_proxies = []

    # 遍历所有代理信息
    for proxy_info in proxies:
        # 获取代理的IP地址
        ip = proxy_info.get("IP地址")
        # 获取代理的端口
        port = proxy_info.get("端口")
        # 获取代理的类型
        proxy_type = proxy_info.get("类型")

        # 检查IP、端口和类型是否都有效
        if ip and port and proxy_type:
            # 构造代理URL
            proxy = f"{proxy_type.lower()}://{ip}:{port}"
            # 检查代理是否可用
            if is_proxy_available(proxy, proxy_type):
                # 如果可用，添加到可用代理列表
                available_proxies.append(proxy)

    # 将可用的代理写入新的文件
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(available_proxies, file, ensure_ascii=False, indent=4)

    return available_proxies
