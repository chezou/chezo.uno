---

title: Configured Pages CMS
date: 2025-08-24 15:11:00+00:00
lastmod: 2025-08-24 15:11:00+00:00
draft: true
featured: false
image:
  preview_only: false
  filename: /pages-cms.png
---

I had been looking for a way to write Hugo articles on mobile devices like my iPad, and that's when I came across this article by mehori and decided to try Pages CMS.

[https://mehori.com/blog/2025/pages-cms/](https://mehori.com/blog/2025/pages-cms/)

To be honest, it doesn't properly support Hugo's folder structure (`/articlename/index.md`), which makes image uploads a bit tricky. On top of that, I couldn't upload images from my iPhone because of a 413 error. But, since I was able to set up and write text-only articles in Japanese from my iPad, I'll count it as a win.

Along the way, I ran into a very minor YAML frontmatter parsing error, but I was able to find a workaround. [https://github.com/pages-cms/pages-cms/issues/308](https://github.com/pages-cms/pages-cms/issues/308)

It's a platform where you can figure things out by reading the code, and it has the bare minimum functionality, so it's good enough for my needs.

Here are my current settings: [https://github.com/chezou/chezo.uno/blob/438a1b6895cc0dc25386e926922382bba5ed38f4/.pages.yml](https://github.com/chezou/chezo.uno/blob/438a1b6895cc0dc25386e926922382bba5ed38f4/.pages.yml)

I also migrated from **wowchemy** to **hugo-blox**, which was quite a hassle. You can find more details in the PR. But seriously, the names have changed way too many times: **Hugo Academic** -> **Wowchemy** -> **Hugo Blox**...

*   [https://github.com/chezou/chezo.uno/pull/50](https://github.com/chezou/chezo.uno/pull/50)
    
*   I also fixed an issue where Amazon affiliate images weren't showing up by changing the settings to not display images. [https://github.com/chezou/chezo.uno/commit/95aad549ee3554bacb560d39dfb51d1499207aa8](https://github.com/chezou/chezo.uno/commit/95aad549ee3554bacb560d39dfb51d1499207aa8) [https://github.com/chezou/chezo.uno/commit/861182ece0c398787306c242b7f3c558508b8d43](https://github.com/chezou/chezo.uno/commit/861182ece0c398787306c242b7f3c558508b8d43)
    

After the migration, I realized the search wasn't working, but I managed to get it running by:

*   Adding a setting to create a **pagefind** index in the Cloudflare build command -> `&& npx pagefind --source 'public'`
    
*   Trying various things with **Cloudflare's Rocket Loader**, but it didn't work, so I ended up disabling it.
    

Now it's working somehow, but it seems like the Japanese search won't work properly. Oh well, what can you do?