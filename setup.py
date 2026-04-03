from pathlib import Path

from setuptools import find_packages, setup


def read_requirements() -> list[str]:
	req_file = Path(__file__).with_name("requirements.txt")
	if not req_file.exists():
		return []
	return [
		line.strip()
		for line in req_file.read_text(encoding="utf-8").splitlines()
		if line.strip() and not line.strip().startswith("#")
	]


setup(
	name="upratham-digital-twin",
	version="0.1.0",
	author="Prathamesh Uravane",
	author_email="upratham200@gmail.com",
	description="Digital twin project notebooks and package code.",
	long_description=Path("README.md").read_text(encoding="utf-8"),
	long_description_content_type="text/markdown",
	python_requires=">=3.10",
	package_dir={"": "src"},
	packages=find_packages(where="src"),
	install_requires=read_requirements(),
)
