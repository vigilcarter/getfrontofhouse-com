# Front of House

Source for [getfrontofhouse.com](https://getfrontofhouse.com). AI-assisted restaurant growth operation. Metro Detroit.

## Structure

```
site/
  index.html            single page
  styles.css            shared styles
  favicon.svg
  vercel.json           hosting config
  robots.txt
  sitemap.xml
  images/               before/after assets (placeholder until generated)
```

## Local preview

```
cd site
python -m http.server 8000
```

Open http://localhost:8000.

## Deploy

GitHub repo `vigilcarter/getfrontofhouse-com`. Vercel auto-deploys from `main`.

```
git add .
git commit -m "describe the change"
git push
```

## Notes

- Palette: cream `#faf5ec` background, near-black `#1a1614` text, terracotta `#b5563a` accent.
- Typography: Source Serif 4 for headlines, Inter for body.
- No em-dashes anywhere in the copy. Hard rule.
- Pricing intentionally absent on the page. Quoted in the reply to the cold email after seeing the restaurant.

## Contact

`info@getfrontofhouse.com`
