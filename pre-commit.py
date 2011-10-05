#!/usr/bin/env python

import os

hooks_dir = os.path.dirname(os.path.abspath(__file__))
relative_dir = os.path.join(hooks_dir, '../..')
project_root = os.path.abspath(relative_dir)

git_included_config = os.path.join(project_root, 'config.js')
confidential_config = os.path.join(project_root, '_config.js')

with open(git_included_config, 'rU') as fh:
  git_included_contents = fh.read()

with open(confidential_config, 'rU') as fh:
  confidential_contents = fh.read()

with open(git_included_config, 'w') as fh:
  fh.write(confidential_contents)

with open(confidential_config, 'w') as fh:
  fh.write(git_included_contents)

os.system('git add %s' % git_included_config)

# In the rare case, that config.js is the only file changed,
# this switch will render the commit worthless (since it will
# move the repo into an unchanged state. In this case, we
# revert the changes before exiting.

with os.popen('git st') as fh:
  git_status = fh.read()

if ('nothing to commit' in git_status or
    'no changes added to commit' in git_status):
  msg = '# From pre-commit hook: No commit necessary, ' \
        'sensitive config unchanged. #'
  hash_head = '#' * len(msg)
  print ('%s\n%s\n%s\n\n' % (hash_head, msg, hash_head)),

  with open(git_included_config, 'w') as fh:
    fh.write(git_included_contents)

  with open(confidential_config, 'w') as fh:
    fh.write(confidential_contents)
