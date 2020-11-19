# ws2812-playground

## ideas

Class exposes either inputs or outputs (or both?)
We can wire inputs and outputs

Possible code:

```
read(phone.accelerometer.x)
write(strip.speed)
write(strip.brightness)
write(strip.red)
pipe(phone.accelerometer.x, strip.red)
```