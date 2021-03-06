from setuptools import setup, find_packages

setup(name="prewikka-apps-customcss",
      version="5.1.0",
      author="Prelude Team",
      author_email="support.prelude@c-s.fr",
      url="https://www.prelude-siem.org",
      packages=find_packages(),
      install_requires=["prewikka >= 5.1.0"],
      entry_points={
          "prewikka.views": [
              "CustomCSS = customcss:CustomCSS",
          ],
      },
      package_data={
          "customcss": ["htdocs/css/*.css",
                        "htdocs/js/*.js",
                        "templates/*.mak"],
      },
)
