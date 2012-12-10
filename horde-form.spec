%define prj Horde_Form

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-form
Version:       0.0.2
Release:       %mkrel 7
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



%changelog
* Mon Jul 26 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-7mdv2011.0
+ Revision: 560544
- Increased release for rebuild

* Thu Mar 18 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-6mdv2010.1
+ Revision: 524829
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased rel ver to 2

* Sat Mar 13 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-5mdv2010.1
+ Revision: 518634
- added Requires(post): php-pear
  added Requires(preun): php-pear
  increased release

* Fri Mar 12 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-4mdv2010.1
+ Revision: 518300
- added Requires:php-pear
  increased release to 4
- increased release to 3
- changed Requires(pre) from php-pear to %%{_bindir}/pear

* Thu Mar 11 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-2mdv2010.1
+ Revision: 517906
- added Requires: php-pear-Services_Weather
  bumbed release to 2

* Mon Feb 15 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 506034
- replaced PreReq with Requires(pre)
- import horde-form


