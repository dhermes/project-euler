Project-Euler: Node.js
=========================

[Install][1] `node`.

To run a script, simply execute
```./no<problem number>.js```

For problems that require problem data, the command must
be run from the directory in which the script lives;
I'll be changing this stupid dependency at some point.

The shebang at the top should work with node installed.
If you have node installed as `nodejs` (i.e. on most modern
Linux installs) then you'll need to execute as
```nodejs no<problem number>.js```

Dependencies
============

These can be installed via `npm`:

- [`bigint`][2] ([requires][3] `libgmp`)
- [`optimist`][4] used by `benchmark.js` for argument parsing

[1]: https://github.com/joyent/node/wiki/Installation
[2]: https://github.com/substack/node-bigint
[3]: https://github.com/substack/node-bigint#install
[4]: https://github.com/substack/node-optimist
