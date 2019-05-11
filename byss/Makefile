SHELL := /bin/bash
VIRTUALENV_DIR := .venv
EXEC := ${VIRTUALENV_DIR}/bin/python ${VIRTUALENV_DIR}/bin/gunicorn -c gun.py app.main:app

help:
	@echo "  server      启动 web server"
	@echo "  shell       打开一个加载应用上下文的 shell"
	@echo "  pip         仅初始化后端 python 环境"
	@echo "  url         url 列表"
	@echo "  clean       清理 .pyc 文件"
	@echo "  daemon      以守护进程启动"
	@echo "  status      查看进程"
	@echo "  stop        停止程序"

pip:
	virtualenv $(VIRTUALENV_DIR)
	$(VIRTUALENV_DIR)/bin/pip install -r requirements.txt
	mkdir -p instance
	mkdir -p data
	touch instance/config.py

dev:
	$(VIRTUALENV_DIR)/bin/python manager.py dev

s server:
	$(VIRTUALENV_DIR)/bin/python manager.py server

daemon:
	${EXEC}
	sleep 1
	ps aux | grep -v grep | grep --colour=auto "${EXEC}"

status:
	ps aux | grep -v grep | grep --colour=auto "${EXEC}"

stop:
	kill `ps aux | grep "${EXEC}" | grep -v "grep" | awk '{print $$2}'`

shell:
	$(VIRTUALENV_DIR)/bin/pip install ipython
	$(VIRTUALENV_DIR)/bin/python manager.py shell

url:
	$(VIRTUALENV_DIR)/bin/python manager.py url

clean:
	$(VIRTUALENV_DIR)/bin/python manager.py clean

db:
	$(VIRTUALENV_DIR)/bin/python manager.py db $(ARG)

