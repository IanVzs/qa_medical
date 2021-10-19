all: run

usedockerdb:
	docker pull neo4j:4.3
	docker run -it -d --name neo4j_4_3 -p 7474:7474 -p 7687:7687 neo4j:4.3

init:
	echo "安装依赖包"
	pip install -r requirements.txt
	echo "导入知识图谱数据,数据较多,以小时记"
	echo "5秒后开始入库..."
	sleep 5
	python build_medicalgraph.py

run:
	uvicorn main:app --reload

help:
	@echo "make: must `init` first, only run"
