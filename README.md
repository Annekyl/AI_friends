## AIFriends（未完成）

一个基于 **Django + DRF 后端** 和 **Vue 3 + Vite + Pinia + Vue Router 前端** 的 Web 应用，用来创建、展示和管理「角色卡片」，支持登录注册、个人空间、角色创建编辑删除、首页无限滚动等功能。

---

### 功能概览

- **用户账号**
  - 用户注册 / 登录 / 登出
  - 基于 JWT 的身份认证（`rest_framework_simplejwt`）
  - 使用 `access token + refresh token`，前端自动在请求头携带 `Authorization: Bearer <token>`，并在过期时自动刷新

- **用户资料**
  - 用户头像上传和裁剪
  - 用户名 / 个人简介编辑
  - 用户个人空间页（`/user-space/:user_id`），展示该用户创建的角色

- **角色（Character）管理**
  - 创建 / 更新 / 删除角色
  - 每个角色包含：名称、介绍文案、头像图片 `photo`、背景图 `background_image`
  - 图片文件存储在后端 `media/character/...`，删除角色时自动删除旧图片

- **首页展示**
  - 首页角色瀑布流式展示（`HomepageIndex.vue`）
  - 通过 `/api/homepage/index/` 分页加载数据
  - 使用 `IntersectionObserver` 和 `sentinel` 实现无限滚动加载

---

### 技术栈

- **后端**
  - Python / Django 6
  - Django REST framework（`rest_framework`）
  - SimpleJWT（`rest_framework_simplejwt`）
  - SQLite（开发环境）

- **前端**
  - Vue 3（Composition API + `script setup`）
  - Vite
  - Pinia（状态管理）
  - Vue Router 4
  - Tailwind CSS + DaisyUI（样式和组件）
  - Axios（HTTP 请求）

---

### 开发环境快速启动

- **克隆项目**

  ```bash
  git clone <your-repo-url> AIFriends
  cd AIFriends
  ```

- **后端（Django）**

  ```bash
  cd backend
  # 建议先创建虚拟环境（可选）
  # python -m venv venv
  # venv\Scripts\activate

  pip install -r requirements.txt  # 如果没有，可根据实际依赖自行安装 Django/DRF/simplejwt 等
  python manage.py migrate
  python manage.py runserver 0.0.0.0:8000
  ```

  后端默认地址：`http://127.0.0.1:8000/`

- **前端（Vue 3 + Vite）**

  ```bash
  cd frontend
  npm install
  npm run dev
  ```

  前端默认地址：`http://localhost:5173/`

---

### 主要接口（部分）

- **账号相关**（`/api/user/account/...`）
  - `POST /api/user/account/register/` 注册
  - `POST /api/user/account/login/` 登录，返回 `access` 并在 Cookie 中写入 `refresh`
  - `POST /api/user/account/logout/` 退出登录
  - `POST /api/user/account/refresh_token/` 刷新 `access token`
  - `GET  /api/user/account/get_user_info/` 获取当前登录用户信息

- **角色相关**（`/api/create/character/...`）
  - `POST /api/create/character/create/` 创建角色
  - `POST /api/create/character/update/` 更新角色
  - `POST /api/create/character/remove/` 删除角色（需要登录，且只能删除自己创建的角色）
  - `GET  /api/create/character/get_single/?character_id=...` 获取单个角色详情
  - `GET  /api/create/character/get_list/` 获取当前用户的角色列表

- **首页**
  - `GET /api/homepage/index/?items_count=0`  
    返回从 `items_count` 开始的 20 条角色数据，用于首页无限滚动加载。

---

### 目录结构简要说明

- `backend/`：Django 后端工程
  - `backend/settings.py`：Django & DRF & JWT & CORS 等配置
  - `web/`：主要业务应用（用户、角色、首页等）
- `frontend/`：Vue 3 前端工程
  - `src/views/`：各个页面视图
  - `src/components/`：通用组件（如 `NavBar`、`Character` 等）
  - `src/js/http/api.js`：Axios 实例和拦截器

---
