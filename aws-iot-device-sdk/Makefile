#
# Copyright (C) 2010-2014 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=aws-iot-device-sdk
PKG_VERSION:=1.2.0
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL:=https://github.com/aws/aws-iot-device-sdk-python.git
PKG_SOURCE_SUBDIR:=$(PKG_NAME)-$(PKG_VERSION)
PKG_SOURCE_VERSION:=333ffdb00588a7bcd80b21d352d6f4f44597c9a5
PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION)-$(PKG_SOURCE_VERSION).tar.gz

HOST_BUILD_DEPENDS:=python/host

include $(INCLUDE_DIR)/package.mk
$(call include_mk, python-package.mk)

define Package/aws-iot-device-sdk
  TITLE:=aws-iot-device-sdk
  DEPENDS:=+python-light
  SECTION:=lang
  CATEGORY:=Languages
  SUBMENU:=Python
  URL:=https://github.com/aws/aws-iot-device-sdk-python
endef

define Package/aws-iot-device-sdk/description
Amazon AWS IoT SDK for Python
endef

define Build/Compile
	$(call Build/Compile/PyMod,,install --prefix="/usr" --root="$(PKG_INSTALL_DIR)")
endef

$(eval $(call PyPackage,aws-iot-device-sdk))
$(eval $(call BuildPackage,aws-iot-device-sdk))
