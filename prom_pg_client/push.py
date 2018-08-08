from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

registry = CollectorRegistry()
gauge_temperature = Gauge('temperature', 'Current temperature in Celsius', ['location'],
                              registry=registry)
gauge_humidity = Gauge('humidity', 'Current humidity level in %', ['location'],
                    registry=registry)

def to_gateway(location, temperature, humidity, job='romaine'):
    push_gw_svr_path = "pushgateway.romaine.ly.lv"

    gauge_temperature.labels(location).set(temperature)
    gauge_humidity.labels(location).set(humidity)

    push_to_gateway(push_gw_svr_path, job=job, registry=registry)