# HomeRunway — information website

Static Spanish/English privacy, support, estimates and legal information for HomeRunway.

- [Español](site/es/index.html)
- [English](site/en/index.html)

This repository contains the information website only. It does not include the iOS application's source or user data. HTML, CSS and images are served locally, without added analytics, advertising, forms or third-party assets loaded at runtime.

## Build locally

Python 3 standard library only:

```sh
python3 build.py --check-ready
python3 check.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory site
```

Only `site/` is the GitHub Pages artifact. The workflow requires a manual run and complete publication configuration; it does not deploy on push.

© 2026 Gonzalo Peralta Gaudes. Todos los derechos reservados. All rights reserved. Third-party rights remain with their owners. No open-source licence for the application is granted by this repository.
