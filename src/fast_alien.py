from alien import Alien

class FastAlien(Alien):
    """Classe que representa um alienígena mais rápido, herdando da classe Alien."""

    def update(self) -> None:
        """Atualiza a posição do alienígena mais rápido."""
        self.x += (self.settings.alien_speed * 2) * self.settings.fleet_direction
        self.rect.x = self.x