import click
from termcolor import colored
from helpers import *

@click.command()
@click.option(
    '--niveles',
    prompt='Total de niveles',
    help='Total de niveles'
)
@click.option(
    '--pv',
    prompt='PV (multiplo de 13)',
    help='PV por usuario (multiplo de 13)'
)
@click.option(
    '--tipo',
    prompt='Tipo de calculo(reconsumo/afiliacion)',
    help='Calculo de afiliacion o reconsumo'
)
def calcularComision(niveles, pv, tipo):
    try:
        if validarPv(pv):
            if validarTipo(tipo):
                lista_comisiones = Comisiones(niveles, pv, tipo).listar()

                click.echo(colored(f'Total afiliados: {lista_comisiones["total_afiliados"]}', 'blue'))
                click.echo(colored(f"Dinero ingresado: {lista_comisiones['dinero_ingresado']}", 'blue'))
                click.echo(colored(f"Puntos generados: {lista_comisiones['puntos_generados']}", 'blue'))
                click.echo()
                click.echo(colored(f'Comisiones patrocinio: {lista_comisiones["comisiones_patrocinio"]}', 'red'))
                click.echo(colored(f"Comisiones binario: {lista_comisiones['comisiones_binario']}", 'red'))
                click.echo(colored(f"Comisiones mlm: {lista_comisiones['comisiones_mlm']}", 'red'))
                click.echo(colored(f"Total comisiones pagadas: {lista_comisiones['total_comisiones']}", 'red'))
                click.echo()
                click.echo(colored(f"Beneficios en dinero: {lista_comisiones['beneficio_dinero']}", 'green'))
                click.echo(colored(f"Beneficios en (%): {lista_comisiones['beneficio_porcentaje']}", 'green'))
                click.echo()
                click.echo(colored(f"Bronces: {lista_comisiones['bronces']}", 'yellow'))
                click.echo(colored(f"Platas: {lista_comisiones['platas']}", 'yellow'))
                click.echo(colored(f"Oros: {lista_comisiones['oros']}", 'yellow'))
                click.echo(colored(f"Zafiros: {lista_comisiones['zafiros']}", 'yellow'))
                click.echo(colored(f"Rubis: {lista_comisiones['rubis']}", 'yellow'))
                click.echo(colored(f"Diamantes: {lista_comisiones['diamantes']}", 'yellow'))
            else:
                raise Exception('Tipo de calculo no valido (reconsumo/afiliacion)')
        else:
            raise Exception('El paquete debe ser multiplo de 13 (Ejemplo: 13, 26, 39, 52, 65, 78, 91), que es el equivalente a un producto de 150 soles en Perú')
    except Exception as e:
        click.echo(colored(f"Error: {e}", 'red'))
    finally:
        input('Presione cualquier tecla para finalizar...')

if __name__ == '__main__':
    calcularComision()