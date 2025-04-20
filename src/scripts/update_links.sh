#!/bin/bash

# 更新中文页面中的导航链接
echo "Updating Chinese pages..."
for file in cn/*.html; do
  echo "Processing $file"
  # 更新导航菜单中的链接，移除.html后缀
  sed -i '' 's|href="index.html"|href="/cn"|g' "$file"
  sed -i '' 's|href="filter.html"|href="/cn/filter"|g' "$file"
  sed -i '' 's|href="diagnostic.html"|href="/cn/diagnostic"|g' "$file"
  sed -i '' 's|href="governance.html"|href="/cn/governance"|g' "$file"
  sed -i '' 's|href="detail.html"|href="/cn/detail"|g' "$file"
  
  # 更新英文切换链接，使用绝对路径
  case $(basename "$file") in
    "index.html")
      sed -i '' 's|href="../en/index.html"|href="/en"|g' "$file"
      ;;
    "filter.html")
      sed -i '' 's|href="../en/filter.html"|href="/en/filter"|g' "$file"
      ;;
    "diagnostic.html")
      sed -i '' 's|href="../en/diagnostic.html"|href="/en/diagnostic"|g' "$file"
      ;;
    "governance.html")
      sed -i '' 's|href="../en/governance.html"|href="/en/governance"|g' "$file"
      ;;
    "detail.html")
      sed -i '' 's|href="../en/detail.html"|href="/en/detail"|g' "$file"
      ;;
  esac
done

# 更新英文页面中的导航链接
echo "Updating English pages..."
for file in en/*.html; do
  echo "Processing $file"
  # 更新导航菜单中的链接，移除.html后缀
  sed -i '' 's|href="index.html"|href="/en"|g' "$file"
  sed -i '' 's|href="filter.html"|href="/en/filter"|g' "$file"
  sed -i '' 's|href="diagnostic.html"|href="/en/diagnostic"|g' "$file"
  sed -i '' 's|href="governance.html"|href="/en/governance"|g' "$file"
  sed -i '' 's|href="detail.html"|href="/en/detail"|g' "$file"
  
  # 更新中文切换链接，使用绝对路径
  case $(basename "$file") in
    "index.html")
      sed -i '' 's|href="../cn/index.html"|href="/cn"|g' "$file"
      ;;
    "filter.html")
      sed -i '' 's|href="../cn/filter.html"|href="/cn/filter"|g' "$file"
      ;;
    "diagnostic.html")
      sed -i '' 's|href="../cn/diagnostic.html"|href="/cn/diagnostic"|g' "$file"
      ;;
    "governance.html")
      sed -i '' 's|href="../cn/governance.html"|href="/cn/governance"|g' "$file"
      ;;
    "detail.html")
      sed -i '' 's|href="../cn/detail.html"|href="/cn/detail"|g' "$file"
      ;;
  esac
done

echo "Link update completed!" 