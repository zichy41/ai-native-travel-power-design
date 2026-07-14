# Engineering Sources / 工程参考资料

## USB-C / USB Power Delivery

1. USB-IF — USB Charger (USB Power Delivery)  
   USB PD 3.1 将 USB-C 供电能力从此前的 100W 扩展到最高 240W。  
   https://www.usb.org/usb-charger-pd

2. USB-IF — USB Power Delivery Compliance Test Specification  
   包含 Source Capabilities、Status、Battery Status Change、Source Input Change 等协议与测试概念。  
   https://www.usb.org/sites/default/files/USB%20PD3%20CTS%20rev1%20v1.2%20RC20.pdf

3. Infineon — EZ-PD CCG7x consumer USB-C PD & DC-DC controller  
   官方参考设计说明双口 USB-PD、动态共享和可编程控制器是可实现路径。  
   https://www.infineon.com/products/universal-serial-bus/usb-c-ac-dc-and-dc-dc-charging-solutions/ez-pd-ccg7x-consumer-usb-c-power-delivery-dc-dc-controller

4. Infineon — USB-C AC-DC and DC-DC charging solutions  
   官方产品组合覆盖 18W–140W 单口和多口充电器。  
   https://www.infineon.com/products/universal-serial-bus/usb-c-ac-dc-and-dc-dc-charging-solutions

5. Texas Instruments — Engineer's Guide to Current Sensing  
   INA228 等数字功率监测器可测量电流、电压、功率、能量和电荷。  
   https://www.ti.com/lit/eb/slyy154a/slyy154a.pdf

## 插头与地区适配

6. IEC — World Plugs  
   不同地区插头具有不同几何、额定值和接地结构。  
   https://www.iec.ch/world-plugs

## 安克现有产品边界

7. Anker Nano Travel Adapter A9215  
   约 107g；单 USB-C 最高 20W；官方明确不是电压转换器。  
   https://www.anker.com/products/a9215

8. Anker Prime 67W GaN Wall Charger  
   通过较短堆叠式结构和部分包覆插脚强调壁插稳定性。  
   https://www.anker.com/products/a2669-3-port-wall-charger

9. Anker Prime 67W vs GaNPrime 65W  
   官方比较页面明确称重新设计的外形提高墙插稳定性。  
   https://service.anker.com/uk/article-description/What-are-the-differences-between-Anker-Prime-67W-Charger-and-Anker-GaNPrime-65W-Charger

## 使用原则

这些来源用于证明：

- USB-C 多口和功率监测在工程上有实现路径；
- USB PD 存在状态与协商信息；
- 不同地区插头必须按当地结构和要求设计；
- 安克已经关注壁插稳定，因此 Atlas 必须在旅行短线与完整性确认上进一步差异化。

它们不能证明：

- Atlas 已经满足任何标准；
- 所有设备都会返回电池状态；
- 产品已经通过温升、EMC 或安规测试；
- 100W 三口分配已经完成硬件验证。
