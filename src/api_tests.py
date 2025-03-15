from locust import HttpUser, task, between

# Locust Load Testing Class
class APITestUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_text(self):
        self.client.get("/text")

    @task
    def test_compute(self):
        self.client.get("/compute")

    @task
    def test_sleep(self):
        self.client.get("/sleep")
