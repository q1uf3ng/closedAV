---
title: README
updatedAt: 2024-11-02T14:37:33.601Z
createdAt: 2024-11-02T14:28:44.687Z
---

# ClosedAV



`ClosedAV` 是一个用Python编写的工具，旨在帮助用户模拟关闭某些流行的安全软件（如360安全卫士、火绒等）的过程。本工具支持Windows 7/10/11以及Server 2012/2019操作系统,所以理论上讲不需要权限和被标记的风险，也无需驱动

**注意：** 本工具仅供合法授权的测试使用，请勿用于非法目的或未经许可的操作系统上。不当使用可能导致系统不稳定或数据丢失。
### 程序介绍
- 本程序旨在提供一个在过渡到后渗透利用的kill AV程序；
- 目前支持360安全卫士、火绒等主流安全软件，后续会添加更多
- 兼容Windows 7/10/11及Server 2012/2022等
- 模拟用户操作，实现安全软件的关闭
我们的开发实现步骤也很简单，读取pid识别杀软，获取系统和分辨率 图像识别
## 安装

### 依赖项

确保你的环境中已安装以下Python库：

- `pyautogui`：用于模拟用户输入
- `psutil`：用于进程管理和监控
- `opencv`：用于识别

可以通过以下命令安装所需的库：

```bash
pip install pyautogui psutil opencv-python
```
欢迎Issue
开发者:q1uf3ng Bytegeek
微信公众号![qrcode_for_gh_45a25e2baa91_430](https://github.com/user-attachments/assets/f0e84ee1-7c6b-4302-b450-db3b0369bdfa)
