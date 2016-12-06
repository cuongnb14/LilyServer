all: up

up:
	docker-compose up -d

stop:
	docker-compose stop

start:
	docker-compose start

sstart:
	docker-compose start mysql redis

restart:
	docker-compose restart lily

pull-restart:
	git pull && docker-compose restart lily

restart-nginx:
	docker exec -it nginx nginx -s reload

rmcache:
	docker exec -it lilyserver_redis_1 redis-cli flushall
