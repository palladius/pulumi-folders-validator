"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage
import pulumi_github as github

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('pulumi-github-test', location="EU")

# Export the DNS name of the bucket
pulumi.export('bucket_name', bucket.url)

# API Doc here: https://www.pulumi.com/registry/packages/github/api-docs/repository/
repo = github.Repository("pulumized-demo-repo",
  description="Generated from Pulumi from pulumi-folders-validator repo.",
  visibility="private",
)

pulumi.export('gh_repo_name', repo.full_name)

#carlessian_url = lambda repo: f"https://github.com/{repo.full_name}"

pulumi.export('carlessian_url',
    repo.full_name.apply(lambda x: f"https://github.com/{x}")
)

