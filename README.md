# Synopsis
This is just a place to contain various hacks/scripts I've come up with to help me deal with some minor issues I've run into.

# Installation
You should be able to just copy the repository and run the files. Note that some of them may only work on Unix based systems.

# Usage

## django_template_hierarchy.py
``` bash
python django_template_hierarchy_py /var/www/djangoproject/
```

This should give you a quick view of the hierarchy of the Django template "includes" and "extends" commands in your project. For example:
``` python
{ 'templates/error.html': {'templates/404.html': {}, 'templates/500.html': {}},
  'templates/home.html': {'templates/registration/registration_form.html': {},
                         'templates/registration/registration_home.html': {},
                         'templates/registration/registration_submitted.html': {}}
}
```

# License

Copyright 2012 Dan Goldin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.