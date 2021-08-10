Running CI workflow with GitHub Actions:
    1. Merge changes with Dev branch
    2. Workflow will automatically build the container and publish to GitHub Container Registry
    3. Container will be ready to pull from "ghcr.io/bclaydonlight/devops_take_home_test:dev"

Container setup:
    1. docker pull ghcr.io/bclaydonlight/devops_take_home_test:dev
    2. docker run -p 8000:5000 ghcr.io/bclaydonlight/devops_take_home_te:dev
    3. Navigate to "http://127.0.0.1:8000/?url=https://imgs.xkcd.com/comics/bad_code.png" in browser


An additional function has been added to image_augmentations to skew the image alongside the ability to combine all functions. Please note, due to time constraints the Skew function causes the unit test to fail due to the Y axis of the image increased. 