import math
from django.shortcuts import render


def index(request):
    context = {
        "diameter_mm": "",
        "slope_percent": "",
        "manning_n": "0.013",
        "result": None,
        "error": None,
    }

    if request.method == "POST":
        diameter_str = request.POST.get("diameter_mm", "").strip()
        slope_str = request.POST.get("slope_percent", "").strip()
        n_str = request.POST.get("manning_n", "").strip()

        context["diameter_mm"] = diameter_str
        context["slope_percent"] = slope_str
        context["manning_n"] = n_str

        try:
            diameter_mm = float(diameter_str)
            slope_percent = float(slope_str)
            manning_n = float(n_str)

            if diameter_mm <= 0 or slope_percent <= 0 or manning_n <= 0:
                context["error"] = "管徑、坡度與曼寧粗糙係數 n 皆須大於 0。"
            else:
                # 單位轉換：mm -> m, % -> m/m
                d_m = diameter_mm / 1000.0
                slope = slope_percent / 100.0

                # 圓形管滿流幾何性質
                area = math.pi * (d_m ** 2) / 4.0
                hydraulic_radius = d_m / 4.0

                # 曼寧公式：V = (1 / n) * R^(2/3) * S^(1/2)
                velocity = (1.0 / manning_n) * (hydraulic_radius ** (2.0 / 3.0)) * math.sqrt(slope)
                flow_rate = area * velocity

                context["result"] = {
                    "diameter_m": round(d_m, 4),
                    "area": round(area, 6),
                    "hydraulic_radius": round(hydraulic_radius, 6),
                    "slope_ratio": round(slope, 6),
                    "velocity": round(velocity, 4),
                    "flow_rate": round(flow_rate, 6),
                }
        except ValueError:
            context["error"] = "請輸入有效的數值。"

    return render(request, "calculator/index.html", context)
