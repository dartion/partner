/*
 * partner -   bower-version-update.js
 * Description:
 * Author:           darshan
 * Created:          21 Dec. 2019
 * Source:           https://github.com/dartion/partner
 * License:          Copyright (c) 2019 DN - All Rights ReservedAll Rights Reserved
 *                   Unauthorized copying of this file, via any medium is
 *                   strictly prohibited. Proprietary and confidential
 */

#!/usr/bin/env node

'use strict';

var path = require('path');
var packageJSON = require(path.join(__dirname, 'package.json'));
var bowerFile = path.join(__dirname, 'bower.json');
var bowerJSON = require('bower-json').parse(
  require(bowerFile),
  {normalize: true}
);
bowerJSON.version = packageJSON.version;
require('fs').writeFileSync(
  bowerFile,
  JSON.stringify(bowerJSON, null, 2) + '\n'
);
