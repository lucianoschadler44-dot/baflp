# Release Workflow
1. Update `CHANGELOG.md` and `VERSION`.
2. Tag: `git tag vX.Y.Z && git push --tags`.
3. `.github/workflows/release.yml` builds all formats, packages them, writes `SHA256SUMS.txt`,
   and publishes a GitHub Release. History is preserved permanently.
