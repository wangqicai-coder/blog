#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
交易心理学博客文章生成器 - 完整版
2025年1月1日 - 2025年11月15日（319篇）
"""

import sys
import os

# 添加当前目录到路径
sys.path.insert(0, '/home/user/blog')

# 导入所有主题
from generate_trading_psychology_articles import (
    ARTICLE_TOPICS as JAN_APR_TOPICS,
    generate_article_content,
    generate_case_intro,
    generate_concept_section,
    generate_psychology_mechanism,
    generate_neuroscience_section,
    generate_trading_scenario,
    generate_china_market_section,
    generate_practice_step,
    generate_reflection,
    generate_quote
)

from topics_may_to_november import ALL_TOPICS as MAY_JUL_TOPICS
from topics_august_to_november import ALL_TOPICS_AUG_NOV

# 整合所有主题
ALL_ARTICLE_TOPICS = {}
ALL_ARTICLE_TOPICS.update(JAN_APR_TOPICS)
ALL_ARTICLE_TOPICS.update(MAY_JUL_TOPICS)
ALL_ARTICLE_TOPICS.update(ALL_TOPICS_AUG_NOV)

def main():
    """主函数：生成所有文章"""
    print("=" * 70)
    print("🚀 交易心理学系列文章生成器".center(70))
    print("📅 2025年1月1日 - 2025年11月15日（319篇）".center(70))
    print("=" * 70)
    print()

    # 统计信息
    print(f"📊 主题统计:")
    print(f"   总主题数: {len(ALL_ARTICLE_TOPICS)}")
    print()

    # 按月份统计
    month_counts = {}
    for date_str in ALL_ARTICLE_TOPICS.keys():
        month = date_str[:7]  # YYYY-MM
        month_counts[month] = month_counts.get(month, 0) + 1

    for month in sorted(month_counts.keys()):
        month_name = {
            '2025-01': '1月（交易心理基础）',
            '2025-02': '2月（自我认知与交易人格）',
            '2025-03': '3月（恐惧与贪婪的解构）',
            '2025-04': '4月（纪律与一致性系统）',
            '2025-05': '5月（认知偏差与决策陷阱）',
            '2025-06': '6月（最佳流程与绩效优化）',
            '2025-07': '7月（风险认知与仓位管理心理）',
            '2025-08': '8月（信念系统与交易哲学）',
            '2025-09': '9月（压力管理与心理韧性）',
            '2025-10': '10月（影响力与社会心理）',
            '2025-11': '11月（整合与升华）',
        }.get(month, month)
        print(f"   {month_name}: {month_counts[month]}篇")

    print()
    print("=" * 70)
    print()

    # 确认生成
    print("⚠️  即将生成 319 篇文章到 content/posts/ 目录")
    print("   每篇文章约1200-1800字，总计约40-60万字")
    print()

    # 开始生成
    total_generated = 0
    errors = []

    for date_str, topic_info in sorted(ALL_ARTICLE_TOPICS.items()):
        try:
            # 生成文章内容
            content = generate_article_content(date_str, topic_info)

            # 文件路径
            filename = f"{date_str}-{topic_info['slug']}.md"
            filepath = os.path.join("/home/user/blog/content/posts", filename)

            # 写入文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            total_generated += 1

            # 进度显示
            progress = (total_generated / 319) * 100
            print(f"✅ [{total_generated:03d}/319] ({progress:5.1f}%) {date_str} - {topic_info['title']}")

        except Exception as e:
            error_msg = f"❌ 错误: {date_str} - {topic_info['title']} - {str(e)}"
            print(error_msg)
            errors.append(error_msg)

    # 完成总结
    print()
    print("=" * 70)
    if errors:
        print(f"⚠️  完成，但有 {len(errors)} 个错误:")
        for error in errors:
            print(f"   {error}")
    else:
        print("🎉 成功！所有文章已生成")

    print()
    print(f"📈 统计:")
    print(f"   成功生成: {total_generated} 篇")
    print(f"   失败: {len(errors)} 篇")
    print(f"   成功率: {(total_generated/(total_generated+len(errors))*100):.1f}%")
    print()
    print(f"📁 文件位置: /home/user/blog/content/posts/")
    print(f"   文件名格式: YYYY-MM-DD-slug.md")
    print()
    print("=" * 70)
    print()
    print("💡 下一步:")
    print("   1. 检查生成的文章质量")
    print("   2. 运行 hugo server 预览")
    print("   3. 提交到 Git 仓库")
    print()
    print("📚 这319篇文章涵盖了交易心理学的完整体系:")
    print("   • 认知基础（概率思维、信念系统）")
    print("   • 情绪管理（恐惧、贪婪、压力）")
    print("   • 行为控制（纪律、一致性、习惯）")
    print("   • 决策优化（认知偏差、绩效流程）")
    print("   • 风险管理（仓位心理、风险认知）")
    print("   • 社会影响（从众、权威、独立思考）")
    print("   • 哲学整合（信念、意义、人生）")
    print()
    print("🙏 祝您的交易心理修炼之旅顺利！")
    print("=" * 70)

if __name__ == "__main__":
    main()
