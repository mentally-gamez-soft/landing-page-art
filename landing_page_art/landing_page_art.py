"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

CODING_COLORS: bool = False


class State(rx.State):
    link_is_clicked: bool = False

    is_valid_code: bool = False
    is_valid_email: bool = False
    is_valid_url: bool = False

    is_valid_form: bool = False

    @rx.event
    def toggle_link_state(self):
        self.link_is_clicked = not self.link_is_clicked

    @rx.event
    def display_form(self):
        self.link_is_clicked = True


def form_block() -> rx.Component:
    return rx.vstack(
        rx.divider(
            margin_top="1em",
        ),
        rx.hstack(
            rx.card(
                rx.heading(
                    "Invitation code",
                    size="5",
                    justify="center",
                    width="100%",
                ),
                rx.divider(margin_bottom=".5em"),
                rx.hstack(
                    rx.icon("qr-code", size=40),
                    rx.input(
                        name="invite-code",
                        placeholder="OYcFgBeN3WszTa",
                        required=True,
                    ),
                ),
                width="33%",
            ),
            rx.card(
                rx.heading(
                    "Email",
                    size="5",
                    justify="center",
                    width="100%",
                ),
                rx.divider(margin_bottom=".5em"),
                rx.hstack(
                    rx.icon("at-sign", size=40),
                    rx.input(
                        name="email",
                        placeholder="pepito@gmail.com",
                        required=True,
                    ),
                ),
                width="33%",
            ),
            rx.card(
                rx.heading(
                    "Social",
                    size="5",
                    justify="center",
                    width="100%",
                ),
                rx.divider(margin_bottom=".5em"),
                rx.hstack(
                    rx.icon("link", size=40),
                    rx.input(
                        name="url",
                        placeholder="www.mysite.com",
                        required=True,
                    ),
                ),
                width="33%",
            ),
            width="100%",
        ),
        rx.cond(
            State.is_valid_form,
            rx.button("Yeah let's do this!"),
        ),
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        # rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading(
                "ObZcura.",
                size="9",
                margin_bottom="3em",
            ),
            rx.text(
                "This fall, be part of a new chapter in Art industry where analog and digital art are finally One.",
                size="5",
            ),
            rx.text(
                rx.link("I have my invitation code.", href="#"),
                on_click=State.display_form(),
                weight="medium",
                color_scheme="gold",
                high_contrast=True,
            ),
            rx.cond(
                State.link_is_clicked,
                form_block(),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        # rx.logo(),
    )


app = rx.App()
app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="sky",
        grayColor="olive",
        scaling="95%",
    )
)
app.add_page(index)
