"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage
import pulumi_github as github

repo = github.Repository("demo-repo",
  description="Generated from automated test",
  visibility="private",
)

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('pulumi-github-test', location="EU")

# Export the DNS name of the bucket
pulumi.export('bucket_name', bucket.url)
#pulumi.export('gh_repo_name', repo.url)

