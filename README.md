# vibeProxyPool

## 项目简介
`vibeProxyPool` 是一个用于获取多个来源的代理 IP 的工具。该项目支持从多个网站获取免费代理 IP，并提供了命令行工具方便用户使用。

## 安装说明
### 依赖安装
确保你已经安装了 Python 3.x，并且安装了以下依赖包：
~~~bash
 pip install requests beautifulsoup4 selenium
~~~
### 配置 ChromeDriver
1. 下载与你的 Chrome 浏览器版本匹配的 ChromeDriver。
2. 将 ChromeDriver 放在项目目录的 `chromedriver-win64` 文件夹中，并确保 `chromedriver.exe` 文件存在。

## 使用说明
### 命令行参数
使用 `run.py` 脚本可以通过命令行参数来获取代理 IP。以下是可用的命令行参数：

| 参数 | 描述 |
|------|------|
| `-z`, `--run-zdaye` | 使用 zdaye 获取代理池 IP（高质量/支持全系统/容易被封 IP） |
| `-i`, `--run-ihuan` | 使用 ihuan 获取代理池 IP（高质量/仅支持 Windows） |
| `-ip36`, `--run-ip3366` | 使用 ip3366 获取代理池 IP（中质量/支持全系统） |
| `-pr`, `--run-proxylistplus` | 使用 proxylistplus 获取代理池 IP（中质量/支持全系统） |
| `-a`, `--run-all` | 运行所有参数（默认不使用 `-i` 参数，如果你是 Windows 系统，请手动添加 `-i` 参数） |
| `-op`, `--run-openproxy` | 使用 openproxy 源获取 socks4 代理池（中质量/当前全系统可用） |
| `-O`, `--save-output` | 将获取到的 IP 池存放在 `output` 目录中的 `proxies.json` 文件中 |

### 示例
1. 运行所有参数并将结果保存到文件：
~~~bash 
python run.py -a -O
~~~
2. 仅使用 zdaye 和 ip3366 获取代理 IP：
~~~bash 
python run.py -z -ip36
~~~
3. 仅使用 openproxy 获取代理 IP：
~~~bash 
python run.py -op
~~~
## 配置说明
### URL 配置
在 `data/canshu.py` 文件中，你可以找到各个网站的 URL 和请求头配置。根据需要修改这些配置。

### ChromeDriver 配置
确保 `data/canshu.py` 文件中的 `driver_path` 和 `chrome_path` 变量指向正确的 ChromeDriver 和 Chrome 浏览器路径。

### 本项目来自 B站 UP 疯狂的杨CC 二次开发
### QQ交流群:660264846  B站：疯狂的杨CC
![image](https://github.com/user-attachments/assets/aa6099f8-d09d-4a93-b781-30ce705499cd)
### 修改
* 对比原UP主的代码，做了大量修改，增加了新的功能，如：
* 添加了代理池的保存功能，将获取到的代理池保存到本地JSON文件 并指定 文件的编码格式 为UTF_8，方便后续使用以及避免文件编码格式造成的乱码。
* 升级 代码中的不合理的地方 优化代码
* run.py
  1. 异常处理：在 try 块中执行主要逻辑，捕获并打印任何异常。
  2. 资源管理：在 finally 块中确保 StringIO 资源正确释放。
  3. 输入验证：虽然当前代码没有明显的输入验证需求，但可以在未来扩展中加入更多的输入验证逻辑。
  4. 在原来的基础上 加了代理过滤的功能 但是一个都过滤不出来
## 许可证
本项目采用 MIT 许可证，详情见 [LICENSE](LICENSE) 文件。

   