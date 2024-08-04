from manim import *

class Main(Scene):
    def construct(self):
        t2c = {"x": RED, "dx": RED}

        tex = MathTex(R"\int {{|x|}} \,{{dx}}", tex_to_color_map=t2c).scale(2)
        self.play(Write(tex))

        self.wait(1)

        self.play(tex.animate.shift(UP*2 + LEFT*2).scale(0.5))

        let_u = MathTex(R"\text{let } u = {{|x|}}", tex_to_color_map={"u": BLUE}).next_to(tex, DOWN)
        let_u[-1][1].set_color(RED)

        du = MathTex(R"du = {{ \frac{|x|}{x} }} {{\,dx}}", tex_to_color_map={"du": BLUE}).next_to(let_u, RIGHT * 2)
        du[2][1].set_color(RED)
        du[2][4].set_color(RED)
        du[-1].set_color(RED)

        let_dv = MathTex(R"\text{let } dv = \,{{dx}}", tex_to_color_map={"dv": YELLOW, "dx": RED}).next_to(let_u, DOWN * 2)

        v = MathTex(R"v = {{x}}", tex_to_color_map={"v": YELLOW, "x": RED}).next_to(let_dv, RIGHT * 2)

        u_animations = [
            FadeIn(let_u[:-1], shift=UP),
            ReplacementTransform(tex[1:4].copy(), let_u[-1])
        ]

        dv_animations = [
            FadeIn(let_dv[:-1], shift=UP),
            ReplacementTransform(tex[-1].copy(), let_dv[-1])
        ]

        self.play(AnimationGroup(*u_animations))
        self.play(FadeIn(du))
        self.play(AnimationGroup(*dv_animations))
        self.play(FadeIn(v))


        group = VGroup(tex, let_u, du, let_dv, v)
        self.play(group.animate.shift(LEFT * 2))

        t2c_udv = {"u": BLUE, "v": YELLOW, "du": BLUE, "dv": YELLOW}
        udv = MathTex(R"\int u \, dv &= uv - \int v \,du", tex_to_color_map=t2c_udv).next_to(group).shift(UP)

        self.play(Write(udv))
        self.play(Write(index_labels(udv)))

        xdx_udv = MathTex(R"\int |x| \,dx &= {{uv}} - \int v \,du", tex_to_color_map=t2c).move_to(udv)

        xdx_indications = [
            Indicate(udv[1:4]),
            Indicate(tex),
            Indicate(let_u[1]),
            Indicate(let_dv[1]),
        ]

        xdx_udv_animations = [
            ReplacementTransform(udv[:4], xdx_udv[:4]),
            ReplacementTransform(tex, xdx_udv[:4]),
            ReplacementTransform(let_u[-1].copy(), xdx_udv[1]),
            ReplacementTransform(let_dv[-1].copy(), xdx_udv[3]),
            FadeOut(let_dv)
        ]

        uv_udv = MathTex(R"\int |x| \,dx &= {{|x|x}} - \int v \,du", tex_to_color_map=t2c_udv).move_to(xdx_udv)
        uv_udv[1][1].set_color(RED)
        uv_udv[1][-1].set_color(RED)

        uv_udv_indication = [
            Indicate(udv[5:7]),
            Indicate(let_u[1]),
            Indicate(v[0])
        ]

        uv_udv_animations = [
            ReplacementTransform(let_u[-1].copy(), uv_udv[1][0]),
            ReplacementTransform(v[-1].copy(), uv_udv[1][-1]),
            ReplacementTransform(udv[5:7], uv_udv[1]),
            FadeOut(let_u)
        ]

        vdu_udv = MathTex(R"{{x}} \, {{ \frac{|x|}{x} }} {{dx}}").move_to(udv[8:]).shift(RIGHT * 0.2)
        # vdu_udv[0].set_color(RED)
        # vdu_udv[2][0][1].set_color(RED)
        # vdu_udv[2][1][0].set_color(RED)
        # vdu_udv[-1].set_color(RED)
        # vdu_udv[1][0][1].set_color(RED)

        # self.play(FadeOut(udv[8:]))
        # self.play(Write(vdu_udv))

        vdu_udv_indication = [
            Indicate(du[0]),
            Indicate(udv[8:]),
            Indicate(v[0]),
        ]

        vdu_udv_animations = [
            # ReplacementTransform(udv[8:], vdu_udv)
            ReplacementTransform(du[2:], vdu_udv[2:]),
            # ReplacementTransform(v[-1].copy(), vdu_udv[1]),
            # FadeOut(du),
            # FadeOut(v)
        ]

        self.play(AnimationGroup(*xdx_indications))
        self.wait(0.5)
        self.play(AnimationGroup(*xdx_udv_animations))
        # self.remove(udv)
        # debug = index_labels(xdx_udv)
        # self.play(Write(debug))

        self.play(AnimationGroup(*uv_udv_indication))
        self.wait(0.5)
        self.play(AnimationGroup(*uv_udv_animations))
        self.play(uv_udv[1].animate.shift(LEFT * .1))
        # debug2 = index_labels(uv_udv)
        # self.play(Transform(debug, debug2))

        self.play(AnimationGroup(*vdu_udv_indication))
        self.wait(0.5)
        self.play(AnimationGroup(*vdu_udv_animations))

        self.wait(1)