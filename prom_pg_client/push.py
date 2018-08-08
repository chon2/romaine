from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

def push_to_gateway(name, temperature, humidity, job='romaine'):
    push_gw_svr_path = "pushgateway.romaine.ly.lv"

    registry = CollectorRegistry()

    gauge_temperature = Gauge('_'.join(name, 'temperature'), 'Current temperature in Celsius', registry=registry)
    gauge_temperature.set(temperature)

    gauge_humidity = Gauge('_'.join(name, 'humidity'), 'Current humidity level in %', registry=registry)
    gauge_humidity.set(humidity)

    push_to_gateway(push_gw_svr_path, job=job, registry=registry)