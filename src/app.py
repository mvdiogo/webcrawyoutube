from dataclasses import dataclass, field

import navegar

qtd_repeticoes = 1
qtd_objetos = 1  # foi testado até 40 cliques ao mesmo tempo
duracao_video = [30, 50]
url = "https://www.youtube.com/watch?v=[seuvideo]"
proxy = "127.0.0.1:9050"  # endereço local do tor


@dataclass()
class Cluster:
    qtd_objetos: int = 1
    qtd_repeticoes: int = 1
    duracao_video: list[int] = field(default_factory=list)
    url: str = "http://www"
    proxy: str = "127.0.0.1:9050"  # endereço local do tor


def main() -> None:
    cluster = Cluster(
        qtd_objetos=qtd_objetos,
        qtd_repeticoes=qtd_repeticoes,
        duracao_video=duracao_video,
        url=url,
        proxy=proxy,
    )
    objs = list()
    print(f"Total de objetos: {cluster.qtd_objetos * cluster.qtd_repeticoes}")
    for num_obj in range(cluster.qtd_objetos):
        objs.append(
            navegar.Navegar(
                cluster.qtd_repeticoes,
                cluster.duracao_video,
                cluster.url,
                cluster.proxy,
                num_obj,
                cluster.qtd_objetos,
            )
        )
        objs[num_obj].start()
        print(f"Número do objeto: {num_obj}")


if __name__ == "__main__":
    main()
