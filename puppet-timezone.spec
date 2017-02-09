%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name puppet-timezone

Name:           puppet-timezone
Version:        3.4.0
Release:        1%{?dist}
Summary:        Manage timezone settings via Puppet.
License:        ASL 2.0

URL:            https://github.com/saz/puppet-timezone

Source0:        https://github.com/saz/%{upstream_name}/archive/v%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Manage timezone settings via Puppet.

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/timezone/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/timezone/



%files
%{_datadir}/openstack-puppet/modules/timezone/


%changelog
* Thu Feb 09 2017 Alfredo Moralejo <amoralej@redhat.com> 3.4.0-1
- Update to 3.4.0


