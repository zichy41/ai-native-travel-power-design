# AI-Native Travel Power Design

> An AI-native product design experiment for a reliable cross-border travel power system.  
> 飞书「AI 先锋未来人才大赛」安克创新命题参赛研究仓库。

## 1. Project Goal / 项目目标

本项目选择安克的**智能充电品类**，探索一套可复用的“AI 原生产品设计与定义工作流”，并用该工作流提出一款面向跨国、多设备旅行者的产品概念。

当前产品假设为：

**Anker Atlas Relay**  
一套采用“轻量地区插头 + 短线式桌面 GaN 主机 + 充电连续性确认”的高可靠旅行供电系统。

核心问题不是“再做一个功率更高、接口更多的旅行充电器”，而是：

> 如何降低陌生、松动、凹陷或位置受限插座中的机械失效风险，并确保用户第二天真正获得可用电量？

## 2. Challenge / 命题要求

安克创新要求参赛者：

1. 选择一个安克品类；
2. 设计并演示一套“AI 原生”的产品设计与定义工作流；
3. 产出用户洞察、产品概念与可行性分析；
4. 对比 AI 驱动方法和传统经验驱动方法的本质差异。

详见 [`docs/00_challenge_brief.md`](docs/00_challenge_brief.md)。

## 3. Experience-Driven Baseline V0 / 经验驱动基线

最初凭个人旅行经验提出的直觉方案是：

> 将 GaN 充电器、地区转换插头、充电宝和线材设计成可自由组合的模块化旅行供电系统。

这一方案存在明显“先有答案、再找理由”的风险。项目因此建立 Baseline V0，随后让 AI 用户替身、公开用户证据、竞品资料和工程模型共同挑战它。

详见 [`docs/02_experience_baseline_v0.md`](docs/02_experience_baseline_v0.md)。

## 4. How AI Changed the Direction / AI 如何改变方向

AI 合成用户情境扩大了场景覆盖，但也暴露出确认偏差和技术幻觉。公开讨论与力学建模进一步提示：

- 重型充电器叠加转换头会显著提高墙端下坠力矩；
- 用户已自发使用短延长线或桌面充电器卸载墙面重量；
- 部分旅行者偏好轻量、目的地明确的地区插头；
- 万能转换头对另一部分用户已经足够，因此产品不应面向所有旅行者；
- “可拆卸电池”“App 提醒”“20%–30% 溢价”目前证据不足。

产品方向由“大而全的模块化旅行供电系统”收敛为：

> **优先解决机械稳定性、地区适配正确性和充电连续性确认。**

## 5. Current Product Hypothesis / 当前产品假设

### Anker Atlas Relay

- **Region Plug Head**：轻量、目的地明确的地区插头模块；
- **Flex-Link**：约 25–30 cm 的柔性短电源线，将重型主机从墙面移至桌面；
- **GaN Power Hub**：面向笔记本、手机、平板与相机的多 USB-C 桌面主机；
- **Charge Assurance**：检测输入中断、端口反复断连和异常低功率，提供本机提示；手机通知为可选功能；
- **V2 可选扩展**：可拆卸电池模块，尚未进入核心版本。

这仍然是**待验证的产品假设**，不是已经被市场证明的结论。

## 6. Engineering Simulation / 工程建模

仓库包含一个简化静力模型，对比三种结构的墙端下坠力矩：

1. 65W 充电器直接插墙；
2. 旅行转换头与 65W 充电器叠加；
3. 轻量墙插头 + 短线 + 桌面主机。

运行：

```bash
pip install -r requirements.txt
python simulation/torque_model.py
```

核心模型：

\[
\tau = m g d
\]

当前基准结果：

| 结构 | 估算下坠力矩 |
|---|---:|
| 65W 直插 | 约 0.043 N·m |
| 转换头 + 65W 充电器 | 约 0.088 N·m |
| 轻量插头 + 短线 | 约 0.0025 N·m |

短线方案相对叠加结构的墙端静态力矩降低约 97%。  
**这不等于真实掉落率降低 97%**，模型只支持“墙端机械负载被显著降低”。

详见 [`simulation/README.md`](simulation/README.md)。

## 7. Repository Contents / 仓库结构

```text
docs/        命题拆解、问题定义、AI 原生工作流、决策日志
research/    合成用户、公开证据、竞品矩阵、假设登记表
simulation/  力矩模型与参数
results/     仿真结果和图表
prototype/   后续交互原型与 Agent 工作流
```

## 8. Evidence Policy / 证据原则

本项目严格区分：

- **真实个人经历**
- **AI 生成的合成用户情境**
- **公开网络用户讨论**
- **官方产品规格**
- **工程数字仿真**
- **未来实体实验**

合成用户不被表述为真实访谈；数字仿真不被表述为已完成实体测量。

详见 [`docs/05_limitations_and_ethics.md`](docs/05_limitations_and_ethics.md)。

## 9. Selected Public Sources / 部分公开来源

- Anker 735 Charger (Nano II 65W), official specifications:  
  https://www.anker.com/products/a2667
- Anker 735 Charger (GaNPrime 65W), official weight and dimensions:  
  https://www.anker.com/nz/products/a2668
- Anker Nano Travel Adapter, official specifications and voltage-conversion note:  
  https://www.anker.com/products/a9215
- Anker Prime 67W design note on enhanced wall stability:  
  https://service.anker.com/uk/article-description/What-are-the-differences-between-Anker-Prime-67W-Charger-and-Anker-GaNPrime-65W-Charger
- Public user report: heavy charger loosening in an outlet:  
  https://www.reddit.com/r/anker/comments/x1og80/anker_735_wall_prongs_so_thin_the_device_falls/
- Public user discussion: travel plug falling from loose sockets:  
  https://www.reddit.com/r/AskElectricians/comments/1bmitef/my_travel_plug_keeps_falling_out_the_sockets_are/
- Public discussion: all-in-one versus country-specific travel adapters:  
  https://www.reddit.com/r/travel/comments/1ir3ymv/travel_adapters_do_you_prefer_the_all_in_one_or/

## 10. Status / 当前状态

- [x] 命题拆解
- [x] 经验驱动 Baseline V0
- [x] AI 合成用户压力测试
- [x] 合成数据偏差审查
- [x] 第一轮公开用户证据整理
- [x] 墙端下坠力矩数字仿真
- [x] 初版产品假设收敛
- [ ] 大规模公开评论编码
- [ ] 真实访谈
- [ ] 实体插座负载实验
- [ ] 多智能体工作流原型
- [ ] 产品概念图与交互原型
- [ ] AI 驱动 vs 经验驱动对照实验

## License

MIT
