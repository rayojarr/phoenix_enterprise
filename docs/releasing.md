# Releasing

**TL;DR.** A pushed, annotated tag `vMAJOR.MINOR[-beta[.N]]` that names `headset.json`'s version makes the
release overpressure downloads (`python -m overpressure headset add phoenix_enterprise`, the window's *Download*): the
source zip and its SHA-256, nothing uploaded by hand. Only the headset's team creates its tags
([GOVERNANCE.md](https://github.com/overpressure/.github/blob/main/GOVERNANCE.md)).

## Versions

`MAJOR.MINOR[-beta[.N]]`, as a Git tag `vMAJOR.MINOR...`, the same as `version` in
[headset.json](../headset.json). A beta is a pre-release: `headset add phoenix_enterprise` takes it while there is no
stable release. `api` in `headset.json` names the overpressure headset interface the release was made for: every
overpressure that runs it installs the release, also later ones.

## A release

1. **Ready.** Everything is on `main`, CI is green, and no issue the release depends on is open.
2. **The version.** Set it in `headset.json`, by pull request.
3. **The tag.** An annotated tag on that commit of `main`: its first line the release's title, the rest the
   release's own words, what was checked on the headset and what is known not to work. Then push it. The first
   beta of a version is `-beta`, the next `-beta.2`.

   ```sh
   git tag -a v0.1-beta -F tag-message.md
   git push origin v0.1-beta
   ```

4. **CI** ([release.yml](../.github/workflows/release.yml)) runs every check of CI on the tagged commit, refuses
   a tag that is not annotated, not on `main` or names another version than `headset.json`, writes the notes and
   `CHANGELOG.md` with overpressure's `scripts/release.py notes` (git-cliff, [cliff.toml](../cliff.toml)), makes
   the source zip with `git archive` and creates the GitHub release, a pre-release for a beta.
5. **The catalogue.** For its first release, the headset gets its entry in overpressure's
   `overpressure/catalogue.py`, by pull request there: then the window offers it.

A failed check stops the release before anything is published. Fix it on `main`, delete the tag (`git push
origin :refs/tags/v0.1-beta`) and tag the fixed commit. A published version never moves.
