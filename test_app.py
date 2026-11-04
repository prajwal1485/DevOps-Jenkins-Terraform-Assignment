
import unittest
import app as task_app


class TaskManagerTestCase(unittest.TestCase):

    def setUp(self):
        task_app.app.config["TESTING"] = True
        self.client = task_app.app.test_client()
        task_app.reset_tasks()

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_default_tasks(self):
        response = self.client.get("/")
        self.assertIn(b"Learn Jenkins CI/CD", response.data)
        self.assertIn(b"Understand Terraform", response.data)

    def test_add_task(self):
        response = self.client.post(
            "/add",
            data={"title": "Complete DevOps Assignment"}
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            any(task["title"] == "Complete DevOps Assignment"
                for task in task_app.tasks)
        )

    def test_complete_task(self):
        self.client.get("/complete/1")

        self.assertTrue(
            next(task for task in task_app.tasks if task["id"] == 1)["completed"]
        )

    def test_delete_task(self):
        self.client.get("/delete/1")

        self.assertFalse(
            any(task["id"] == 1 for task in task_app.tasks)
        )


if __name__ == "__main__":
    unittest.main()
