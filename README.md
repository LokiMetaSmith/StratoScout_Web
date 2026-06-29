# StratoScout_Web


Static website for Startoscout.space and others

 single scrollable page generated from the initial presentation.

## Setup Instructions

### Python Environment
1. Ensure you have Python installed.
2. Install the necessary library:
   ```bash
   pip install aspose.slides
   ```
   *(Note: Depending on your OS, you may need additional libraries like `libgdiplus` or `libssl1.1` as documented by Aspose).*

### How to Convert the Slides
1. Place your `.pptx` file in the root of the project.
2. Ensure the filename matches the one in `scripts/convert_slides.py`.
3. Run the conversion script:
   ```bash
   python scripts/convert_slides.py
   ```
4. This will generate individual slide HTML files in the `slides_html/` directory.
5. The `index.html` file acts as the landing page and will dynamically pull in the contents of `slides_html/`.

## Hosting on GitHub Pages with Namecheap Domain

To self-host this repository on GitHub pages and route it to your Namecheap domain, follow these steps:

### 1. Set up GitHub Pages
1. Push this repository to GitHub.
2. Go to your repository **Settings**.
3. In the left sidebar, click on **Pages**.
4. Under "Build and deployment", select the `main` (or `master`) branch as the source, and `/ (root)` as the folder. Click **Save**.
5. Wait a few minutes for GitHub to build and deploy your site to `username.github.io/repository-name`.

### 2. Configure Namecheap DNS
1. Log into your Namecheap account.
2. Go to **Domain List** and click **Manage** next to your domain.
3. Click on the **Advanced DNS** tab.
4. Under **Host Records**, click **Add New Record** to add the following records:
   - **Type**: `A Record` | **Host**: `@` | **Value**: `185.199.108.153`
   - **Type**: `A Record` | **Host**: `@` | **Value**: `185.199.109.153`
   - **Type**: `A Record` | **Host**: `@` | **Value**: `185.199.110.153`
   - **Type**: `A Record` | **Host**: `@` | **Value**: `185.199.111.153`
   - **Type**: `CNAME Record` | **Host**: `www` | **Value**: `username.github.io` *(Replace `username` with your GitHub username)*.
5. Save all changes (click the green checkmark next to each record).

### 3. Link Custom Domain in GitHub
1. Go back to your GitHub repository **Settings** > **Pages**.
2. Scroll down to the **Custom domain** section.
3. Enter your Namecheap domain name (e.g., `stratoscout.space`).
4. Click **Save**. This will automatically create a `CNAME` file in your repository.
5. Tick the box **Enforce HTTPS** to ensure your site is secure (this might take up to 24 hours to issue the certificate).

Your website will soon be live on your custom Namecheap domain!
