from blog.models import Post, Category
from django.core.management.base import BaseCommand
from typing import Any
import random

class Command(BaseCommand):
    help = "This Command inserts post data" 

    def handle(self, *args:Any, **options: Any):

        Post.objects.all().delete()

        titles = [
            "Getting Started with Django",
            "Understanding Python Basics",
            "How to Build a Blog App",
            "Introduction to REST APIs",
            "Mastering HTML and CSS",
            "JavaScript for Beginners",
            "Working with React Components",
            "State Management in React",
            "Introduction to Databases",
            "Using SQLite with Django",
            "Deploying Your First Web App",
            "Understanding Git and GitHub",
            "Debugging Tips for Developers",
            "Building Responsive Layouts",
            "Introduction to Machine Learning",
            "Data Analysis with Pandas",
            "NumPy Basics Explained",
            "Understanding Virtual Environments",
            "Django Models Deep Dive",
            "Frontend vs Backend Explained"
        ]

        contents = [
            "This is the description for blog post 1. It contains sample content for UI testing.",
            "This is the description for blog post 2. It contains sample content for UI testing.",
            "This is the description for blog post 3. It contains sample content for UI testing.",
            "This is the description for blog post 4. It contains sample content for UI testing.",
            "This is the description for blog post 5. It contains sample content for UI testing.",
            "This is the description for blog post 6. It contains sample content for UI testing.",
            "This is the description for blog post 7. It contains sample content for UI testing.",
            "This is the description for blog post 8. It contains sample content for UI testing.",
            "This is the description for blog post 9. It contains sample content for UI testing.",
            "This is the description for blog post 10. It contains sample content for UI testing.",
            "This is the description for blog post 11. It contains sample content for UI testing.",
            "This is the description for blog post 12. It contains sample content for UI testing.",
            "This is the description for blog post 13. It contains sample content for UI testing.",
            "This is the description for blog post 14. It contains sample content for UI testing.",
            "This is the description for blog post 15. It contains sample content for UI testing.",
            "This is the description for blog post 16. It contains sample content for UI testing.",
            "This is the description for blog post 17. It contains sample content for UI testing.",
            "This is the description for blog post 18. It contains sample content for UI testing.",
            "This is the description for blog post 19. It contains sample content for UI testing.",
            "This is the description for blog post 20. It contains sample content for UI testing."
        ]

        img_urls = [
            "https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/5/800/400",
            "https://picsum.photos/id/6/800/400",
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/11/800/400",
            "https://picsum.photos/id/12/800/400",
            "https://picsum.photos/id/13/800/400",
            "https://picsum.photos/id/14/800/400",
            "https://picsum.photos/id/15/800/400",
            "https://picsum.photos/id/16/800/400",
            "https://picsum.photos/id/17/800/400",
            "https://picsum.photos/id/18/800/400",
            "https://picsum.photos/id/19/800/400",
            "https://picsum.photos/id/20/800/400"
        ]

        categories = Category.objects.all()
        print(categories)

        for title, content, img_url in zip(titles, contents, img_urls):

            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=img_url, category = category)

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))