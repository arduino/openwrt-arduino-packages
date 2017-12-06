#
# Copyright (C) 2010-2014 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=aws-iot-runtime-yun
PKG_VERSION:=2.2.0
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL:=https://github.com/aws/aws-iot-device-sdk-arduino-yun.git
PKG_SOURCE_SUBDIR:=$(PKG_NAME)-$(PKG_VERSION)
PKG_SOURCE_VERSION:=39e62018770f49bcb92451ea7a83faf95c753aa8
PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION)-$(PKG_SOURCE_VERSION).tar.gz

include $(INCLUDE_DIR)/package.mk

define Package/aws-iot-runtime-yun
  TITLE:=aws-iot-runtime-yun
  DEPENDS:=+python-light
  SECTION:=lang
  CATEGORY:=Languages
  SUBMENU:=Python
  URL:=https://github.com/aws/aws-iot-runtime-yun
endef

define Package/aws-iot-runtime-yun/description
Amazon AWS IoT Runtime for Arduino Yun
endef

define Build/Compile
	# NOOP
endef

define Package/aws-iot-runtime-yun/install
	$(INSTALL_DIR) $(1)/usr/lib/python2.7/AWS-IoT-Python-Runtime/
	$(INSTALL_DATA) $(PKG_BUILD_DIR)/AWS-IoT-Python-Runtime/* $(1)/usr/lib/python2.7/AWS-IoT-Python-Runtime/
endef

$(eval $(call BuildPackage,aws-iot-runtime-yun))
