%define prj Horde_Form

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-form
Version:       0.0.2
Release:       %mkrel 6
Summary:       Horde Form API
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(post):php-pear
Requires(preun):php-pear
Requires(pre): php-pear
Requires:      php-gettext
Requires:      horde-framework
Requires:      horde-token
Requires:      horde-util
Requires:      php-pear
Requires:      php-pear-Services_Weather
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
The Horde_Form:: package provides form rendering, validation, and other
functionality for the Horde Application Framework.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde
%dir %{peardir}/Horde/Form
%dir %{peardir}/Horde/Form/Action
%dir %{peardir}/Horde/Form/Type
%{peardir}/Horde/Form.php
%{peardir}/Horde/Form/Action.php
%{peardir}/Horde/Form/Action/conditional_enable.php
%{peardir}/Horde/Form/Action/conditional_setvalue.php
%{peardir}/Horde/Form/Action/reload.php
%{peardir}/Horde/Form/Action/submit.php
%{peardir}/Horde/Form/Action/sum_fields.php
%{peardir}/Horde/Form/Action/updatefield.php
%{peardir}/Horde/Form/Renderer.php
%{peardir}/Horde/Form/Type/tableset.php

