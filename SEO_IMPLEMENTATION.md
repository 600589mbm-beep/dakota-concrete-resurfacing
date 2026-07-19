# Dakota Concrete SEO implementation

Implemented for the GitHub Pages site at:

`https://600589mbm-beep.github.io/dakota-concrete-resurfacing/`

## Technical discovery and indexing

- Correct GitHub Pages canonical URLs on the homepage and each service page.
- `robots.txt` allows crawling and points to the correct GitHub Pages sitemap.
- XML sitemap includes the homepage plus five residential service pages.
- Custom 404 page uses `noindex,follow`.
- Crawlable HTML links connect the homepage, service pages, FAQ, service area, and estimate section.
- The Pages workflow generates a clean `dist` artifact and verifies its payload checksums before deployment.

## Search appearance

- Unique page titles and meta descriptions.
- Open Graph and Twitter metadata.
- Descriptive image alt text near relevant service content.
- Local business, website, service, breadcrumb, and FAQ JSON-LD where relevant.
- Removed unverified placeholder phone, email, and inactive form details from public business markup.

## People-first content

- Added a visible homeowner FAQ.
- Added practical guidance about resurfacing suitability, preparation, Minnesota exposure, maintenance, and replacement warning signs.
- Added five focused residential service pages:
  - Driveway resurfacing
  - Patio resurfacing
  - Pool deck resurfacing
  - Sidewalk and walkway resurfacing
  - Front entry and step resurfacing

## Important follow-up outside the codebase

Google does not guarantee crawling, indexing, or rankings. The site owner should verify the GitHub Pages URL-prefix property in Google Search Console, submit `/sitemap.xml`, inspect the homepage and service URLs, and connect a verified Google Business Profile with consistent real-world business details.
