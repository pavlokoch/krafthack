Public repository with EDA and ML model developed for Krafthack by rainy_days


About the sensors available. We are considering one out of 4 units. 

# Operating conditions
*Power* is the power (watt (joule/s)) generated by the unit. 

*Reactive power* is either generated or absorbed by electric generators to maintain a constant voltage level, commonly referred to as providing “voltage support.” From the viewpoint of efficiency, reactive power may be seen as power loss

*Guide vanes* Adjust the turbine load by adjusting blades that directes the water. Adjusting the vanes will increase or decrease the flow rate through the turbine. Guide vanes are not stationary, they change their angle as per the requirement to control the angle of striking of water to turbine blades to increase the efficiency. They also regulate the flow rate of water into the runner blades thus controlling the power output of a turbine according to the load on the turbine. OBS: They control the angle and amout of water allowed to enter the runner from the water inlet. 

*Draft tube* This is located at the exit end of the turbine and helps to throughput the "used" water. It is at the exit end of the turbine increasing the pressure of the exiting fluid at the expense of its velocity. Think windmills where the air must have some remaining momentum to escape. 

*spiral casing* The spiral casing is the inlet medium of water to the turbine. he water flowing from the reservoir or dam is made to pass through this pipe with high pressure. The blades of the turbines are circularly placed, which means the water striking the turbine’s blades should flow in the circular axis for efficient striking. So the spiral casing is used, but due to the circular movement of the water, it loses its pressure.

*rotational speed* Water enters these turbines radially meaning that it enters the turbine perpendicular to the rotational axis. Once entering the turbine, the water always flows inwards, towards the center. Once the water has flown through the turbine, it exits axially, parallel to the rotational axis.

# Bolt conditions

*Temperature* steel temperature.. this is a consequence of stress on the bolts. Tensile properties depend on temperature. Yield strength, tensile strength, and modulus of elasticity decrease at higher temperatures. Ductility (the ability of a material to be drawn or plastically deformed without fracture) typically increases with temperature (think melted steel bolt can deform without fracturing). 


*6 torsion sensors* [N/m^2 or Pa] is the result of applying torque (twisting of the bolt, - the force is transferred to the bolt in the same direction as the torque is applied (zonal, azimuthal)). I not sure what a torsion sensor is measuring, or how, or why. I the current bolt configuration there should be no significant rotation of the clamping metal. 

*6 tensile sensors* [N/m] tensile stress is parallel to the bolt (think streching the bolt). This force is the result of tightening the bolt, or in this scenario : the water pressure attempting to expand the steel clamped. This force has a fracture point, or a tensile  point. That is, the force the bolt can withstain before fracturing. As the stress increases the bolt goes from an elastic streching regime to a plastic range where is gets deformed. Eventually it breaks.

*clamp length* 70cm? I think it was mentioned in the meeting. 
*torque* [N/m]
*tension* is a result of torque and torsion

# vibrations 
usually measure as a displacement (delta from starting value). Both available sensors connected to the shaft coupling the runner and the generator (image in PDF). Dont know what VRT refers to. 

*lower bearing vibration* 
*turbine bearing vibration* 
https://www.linquip.com/blog/what-is-francis-turbine/


